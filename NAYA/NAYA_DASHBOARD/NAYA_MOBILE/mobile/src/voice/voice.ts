import { SpeechRecognition } from '@capacitor-community/speech-recognition';
export async function listen() {
  await SpeechRecognition.start({ language: 'fr-FR', popup: true });
}
