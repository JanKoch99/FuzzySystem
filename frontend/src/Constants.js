const production = {
  url: "http://localhost:8000",
};
const development = {
  url: "http://localhost:8000",
};
export const config =
  import.meta.env.MODE === "development" ? development : production;
