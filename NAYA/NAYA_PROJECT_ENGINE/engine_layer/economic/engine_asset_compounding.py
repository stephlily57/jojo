# NAYA_PROJECT_ENGINE / ENGINES / engine_asset_compounding.py

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class StrategicAsset:
    origin_project: str
    asset_type: str
    created_at: str


class AssetCompoundingEngine:

    def compound(self, project_name: str) -> StrategicAsset:
        return StrategicAsset(
            origin_project=project_name,
            asset_type="REUSABLE_INFRASTRUCTURE",
            created_at=datetime.utcnow().isoformat()
        )


ENGINE_ASSET_COMPOUNDING = AssetCompoundingEngine()
