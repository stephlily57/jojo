import { Network } from '@capacitor/network';
Network.addListener('networkStatusChange', status => {
  console.log('Network status', status);
});
