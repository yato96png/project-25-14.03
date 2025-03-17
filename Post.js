import React from "react";
import styled from "styled-components";

const PostContainer = styled.div`
  background: white;
  padding: 15px;
  margin: 10px 0;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
`;

const Button = styled.button`
  background: none;
  border: none;
  cursor: pointer;
  font-size: 14px;
  color: ${(props) => (props.like ? "#ff4757" : "#007bff")};

  &:hover {
    text-decoration: underline;
  }
`;

const Post = ({ post, onLike, onRepost }) => (
  <PostContainer>
    <p>{post.content}</p>
    <Button like onClick={() => onLike(post.id)}>❤️ {post.likes}</Button>
    <Button onClick={() => onRepost(post.id)}>🔁 {post.reposts}</Button>
  </PostContainer>
);

export default Post;
