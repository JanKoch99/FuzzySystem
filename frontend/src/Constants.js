const production = {
  url: "https://fuzzysystem.onrender.com/",
};
const development = {
  url: "http://localhost:8000",
};
export const config =
  import.meta.env.MODE === "development" ? development : production;
