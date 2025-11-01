// Simple singleton service to hold form data and fetch image pairs from backend
// Adjust API_BASE_URL as needed or wire to environment variables.
import img1 from "../assets/img1.png";
import img2 from "../assets/img2.png";
import img3 from "../assets/img3.png";
import {config} from "../Constants.js";

const API_BASE_URL = config.url

class DataService {
  constructor() {
    this.userData = null; // { age, budget, relationship, occasion }
    this.otherPersonData = null; // { gender, personality, technical, creative, managerial, academic, style }
    this.imagePairs = null; // array of pairs, e.g., [[url1,url2], ...]
    this.selecteImagePairs = null;
    this.finalImages = null;
  }

  getUserData() {
      return this.userData
  }
  setUserData(data) {
    this.userData = { ...data };
  }

  setOtherPersonData(data) {
    this.otherPersonData = { ...data };
  }

  getImagePairs() {
    return this.imagePairs;
  }

  setSelectedImagePairs(selectedImagePairs) {
      this.selecteImagePairs = selectedImagePairs;
  }

  getFinalImages() {
      return this.finalImages;
  }

  clear() {
    this.userData = null;
    this.otherPersonData = null;
    this.imagePairs = null;
    this.selecteImagePairs = null;
  }

  async fetchImagePairs(signal) {
    if (!this.userData || !this.otherPersonData) {
      throw new Error("Missing userData or otherPersonData before fetching image pairs.");
    }

    const payload = {
      user: this.userData,
      other: this.otherPersonData,
    };

    //TODO: Remove if backend works
    this.imagePairs = [
          [{path: img1, value: 'image1'}, {path: img2, value: 'image2'}],
          [{path: img2, value: 'image2'}, {path: img3, value: 'image3'}],
          [{path: img1, value: 'image1'}, {path: img3, value: 'image3'}],
          [{path: img2, value: 'image2'}, {path: img1, value: 'image1'}],
          [{path: img3, value: 'image3'}, {path: img2, value: 'image2'}],
      ];
    return this.imagePairs

    const url = `${API_BASE_URL}/api/generate-image-pairs`;

    const res = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
      signal,
    });

    if (!res.ok) {
      const text = await res.text().catch(() => "");
      throw new Error(`Failed to fetch image pairs (${res.status}): ${text}`);
    }

    const data = await res.json();
    // Expecting { imagePairs: [[imgA, imgB], ...] }
    this.imagePairs = data?.imagePairs || null;
    return this.imagePairs;
  }

  async fetchFinalImages(signal) {
      if(!this.selecteImagePairs) {
          throw new Error("Missing selected image pairs.");
      }

      const payload = {
          user: this.userData,
          other: this.otherPersonData,
          selectedImages: this.selecteImagePairs
      }

      //TODO: Remove if backend works
      this.finalImages = [
          {path: img1, value: 'image1'},
          {path: img2, value: 'image1'},
          {path: img3, value: 'image1'}
      ]
      return

      const url = `${API_BASE_URL}/api/generate-final-images`;

      const res = await fetch(url, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload),
          signal
      })

      if (!res.ok) {
          const text = await res.text().catch(() => "");
          throw new Error(`Failed to fetch final images (${res.status}): ${text}`);
      }

      const data = await res.json();
      this.finalImages = data?.finalImages || null;
  }
}

const dataService = new DataService();
export default dataService;
