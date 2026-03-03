import { CapacitorConfig } from '@capacitor/cli';
const config: CapacitorConfig = {
  appId: 'com.naya.dashboard',
  appName: 'NAYA Dashboard',
  webDir: '../pwa',
  bundledWebRuntime: false,
  server: { cleartext: true }
};
export default config;
