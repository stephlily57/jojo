"""
NAYA REAPERS - Security Engine

Handles all security, protection, and safety aspects of NAYA ecosystem.

Core responsibilities:
- Access control and authentication
- Audit trail logging
- Integrity verification
- Threat detection
- Emergency shutdown
- Data protection
"""

import hashlib
import json
import logging
from datetime import datetime
from typing import Dict, Any, List, Tuple
from enum import Enum


class SecurityLevel(Enum):
    PUBLIC = 0
    USER = 1
    ADMIN = 2
    SYSTEM = 3


class AuditEvent(Enum):
    LOGIN = "login"
    DATA_ACCESS = "data_access"
    DATA_MODIFY = "data_modify"
    CONFIG_CHANGE = "config_change"
    SECURITY_EVENT = "security_event"
    ERROR = "error"
    SHUTDOWN = "shutdown"


class RapersSecurityEngine:
    """
    REAPERS Security Engine - Protects NAYA ecosystem integrity.

    The name REAPERS (Resilience, Enforcement, Audit, Protection,
    Emergency Response, Safety) encapsulates its function.
    """

    def __init__(self):
        self.audit_log: List[Dict[str, Any]] = []
        self.identity_guard = IdentityGuard()
        self.integrity_verifier = IntegrityVerifier()
        self.threat_detector = ThreatDetector()
        self.encryption_manager = EncryptionManager()
        self.emergency_mode = False

        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='[REAPERS] %(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('REAPERS')

    def authenticate_user(self, user_id: str, credentials: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Authenticate a user.

        Returns: (is_valid, session_token)
        """
        is_valid = self.identity_guard.verify(user_id, credentials)

        if is_valid:
            session_token = self.identity_guard.create_session(user_id)
            self._log_audit(AuditEvent.LOGIN, {
                'user_id': user_id,
                'status': 'SUCCESS',
                'session_token': session_token[:20] + '...'
            })
            return True, session_token
        else:
            self._log_audit(AuditEvent.LOGIN, {
                'user_id': user_id,
                'status': 'FAILED'
            })
            return False, None

    def authorize_action(self, session_token: str, action: str, resource: str) -> bool:
        """
        Check if user is authorized for an action.

        Actions: 'read', 'write', 'delete', 'execute'
        """
        user_id = self.identity_guard.get_user_from_token(session_token)
        if not user_id:
            return False

        is_authorized = self.identity_guard.check_permission(user_id, action, resource)

        self._log_audit(AuditEvent.DATA_ACCESS, {
            'user_id': user_id,
            'action': action,
            'resource': resource,
            'authorized': is_authorized
        })

        return is_authorized

    def verify_integrity(self, data: Dict[str, Any], expected_hash: str) -> bool:
        """
        Verify that data hasn't been tampered with.
        """
        actual_hash = self.integrity_verifier.compute_hash(data)
        is_valid = actual_hash == expected_hash

        self._log_audit(AuditEvent.DATA_ACCESS, {
            'type': 'INTEGRITY_CHECK',
            'valid': is_valid,
            'hash': actual_hash[:32] + '...'
        })

        return is_valid

    def encrypt_sensitive_data(self, data: str) -> str:
        """Encrypt sensitive data."""
        return self.encryption_manager.encrypt(data)

    def decrypt_sensitive_data(self, encrypted: str) -> str:
        """Decrypt sensitive data."""
        return self.encryption_manager.decrypt(encrypted)

    def detect_threat(self, event: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Detect if an event represents a security threat.

        Returns: (is_threat, threat_type)
        """
        threat_detected, threat_type = self.threat_detector.analyze(event)

        if threat_detected:
            self._log_audit(AuditEvent.SECURITY_EVENT, {
                'threat_detected': True,
                'threat_type': threat_type,
                'severity': 'HIGH',
                'action': 'ALERT_ADMIN'
            })

        return threat_detected, threat_type

    def activate_emergency_mode(self, reason: str):
        """Activate emergency protection mode."""
        self.emergency_mode = True

        self._log_audit(AuditEvent.SECURITY_EVENT, {
            'event': 'EMERGENCY_MODE_ACTIVATED',
            'reason': reason,
            'timestamp': datetime.utcnow().isoformat()
        })

        self.logger.warning(f"EMERGENCY MODE ACTIVATED: {reason}")

    def deactivate_emergency_mode(self):
        """Deactivate emergency mode."""
        self.emergency_mode = False

        self._log_audit(AuditEvent.SECURITY_EVENT, {
            'event': 'EMERGENCY_MODE_DEACTIVATED'
        })

    def get_audit_trail(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Get audit trail entries."""
        return self.audit_log[-limit:]

    def _log_audit(self, event_type: AuditEvent, details: Dict[str, Any]):
        """Log an audit event."""
        entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'event_type': event_type.value,
            'details': details
        }
        self.audit_log.append(entry)
        self.logger.info(f"{event_type.value}: {json.dumps(details)}")


class IdentityGuard:
    """Manages user identity and access control."""

    def __init__(self):
        self.users = {}
        self.sessions = {}
        self.permissions = {
            'admin': ['read', 'write', 'delete', 'execute'],
            'user': ['read', 'write'],
            'guest': ['read']
        }

    def verify(self, user_id: str, credentials: Dict[str, Any]) -> bool:
        """Verify user credentials."""
        # Simplified verification - in production use proper auth
        return 'password' in credentials and len(credentials['password']) > 0

    def create_session(self, user_id: str) -> str:
        """Create a user session."""
        session_id = hashlib.sha256(f"{user_id}_{datetime.utcnow()}".encode()).hexdigest()
        self.sessions[session_id] = {
            'user_id': user_id,
            'created_at': datetime.utcnow().isoformat(),
            'role': 'admin'  # Default role
        }
        return session_id

    def get_user_from_token(self, token: str) -> str:
        """Get user ID from session token."""
        session = self.sessions.get(token)
        return session['user_id'] if session else None

    def check_permission(self, user_id: str, action: str, resource: str) -> bool:
        """Check if user has permission for action."""
        # Simplified - always allow admin
        return True


class IntegrityVerifier:
    """Verifies data integrity."""

    def compute_hash(self, data: Dict[str, Any]) -> str:
        """Compute SHA256 hash of data."""
        json_str = json.dumps(data, sort_keys=True)
        return hashlib.sha256(json_str.encode()).hexdigest()

    def verify_signature(self, data: str, signature: str, key: str) -> bool:
        """Verify digital signature."""
        # Simplified verification
        expected_sig = hashlib.sha256(f"{data}{key}".encode()).hexdigest()
        return signature == expected_sig


class ThreatDetector:
    """Detects security threats."""

    def analyze(self, event: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Analyze event for threats.

        Returns: (is_threat, threat_type)
        """
        # Check for multiple failed logins
        if event.get('failed_logins', 0) > 5:
            return True, "BRUTE_FORCE_ATTACK"

        # Check for unusual data access
        if event.get('data_access_count', 0) > 1000:
            return True, "UNUSUAL_DATA_ACCESS"

        # Check for config tampering
        if event.get('config_modified'):
            return True, "UNAUTHORIZED_CONFIG_CHANGE"

        return False, None


class EncryptionManager:
    """Manages data encryption."""

    def encrypt(self, data: str) -> str:
        """Encrypt data (simplified)."""
        # In production, use proper encryption (AES-256, etc)
        return hashlib.sha256(data.encode()).hexdigest()

    def decrypt(self, encrypted: str) -> str:
        """Decrypt data."""
        # In production, use proper decryption
        return encrypted


__all__ = [
    'RapersSecurityEngine',
    'IdentityGuard',
    'IntegrityVerifier',
    'ThreatDetector',
    'EncryptionManager',
    'SecurityLevel',
    'AuditEvent'
]
