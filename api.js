import axios from "axios";

const API_URL = "http://127.0.0.1:5000/posts";

export const getPosts = () => axios.get(API_URL);
export const createPost = (content, parentId = null) =>
  axios.post(API_URL, { content, parent_id: parentId });
export const likePost = (id) => axios.post(`${API_URL}/${id}/like`);
export const repostPost = (id) => axios.post(`${API_URL}/${id}/repost`);
