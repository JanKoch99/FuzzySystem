// Image helper to map backend image paths to frontend imports
import img1 from "../assets/img1.png";
import img2 from "../assets/img2.png";
import img3 from "../assets/img3.png";

// Map of image paths to actual imported images
const imageMap = {
  "/src/assets/img1.png": img1,
  "/src/assets/img2.png": img2,
  "/src/assets/img3.png": img3,
  "img1.png": img1,
  "img2.png": img2,
  "img3.png": img3,
};

/**
 * Get the actual image source from a path string
 * @param {string} path - Image path from backend (can be URL or filename)
 * @returns {string} - Actual image source URL
 */
export function getImageSrc(path) {
  // If it's already a full URL (http/https), return it directly
  if (
    path &&
    typeof path === "string" &&
    (path.startsWith("http://") || path.startsWith("https://"))
  ) {
    return path;
  }

  // If it's already an imported image (data URL), return it
  if (path && typeof path === "string" && path.startsWith("data:")) {
    return path;
  }

  // Check if it's in our map
  if (imageMap[path]) {
    return imageMap[path];
  }

  // Extract filename and try to match
  const filename = path?.split("/").pop();
  if (filename && imageMap[filename]) {
    return imageMap[filename];
  }

  // Default fallback to img1
  return img1;
}

export default imageMap;
