import React, { useEffect, useState } from "react";
import { getPosts, likePost, repostPost } from "../api";
import Post from "../components/Post";
import Header from "../components/Header";

const Feed = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    getPosts().then((res) => setPosts(res.data));
  }, []);

  return (
    <>
      <Header />
      {posts.map((post) => (
        <Post key={post.id} post={post} onLike={likePost} onRepost={repostPost} />
      ))}
    </>
  );
};

export default Feed;
