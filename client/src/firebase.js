// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: import.meta.env.VITE_FIREBASE_API_KEY,
  authDomain: "heartility-99016.firebaseapp.com",
  projectId: "heartility-99016",
  storageBucket: "heartility-99016.appspot.com",
  messagingSenderId: "332745630177",
  appId: "1:332745630177:web:ebdafad1ae925c6e5872a0",
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);