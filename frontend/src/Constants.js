const production = {
    url: 'todo'
};
const development = {
    url: 'http://localhost:4000'
};
export const config = import.meta.env.MODE === 'development' ? development : production;