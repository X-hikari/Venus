<template>
  <div>

    <!-- 标题部分 -->
    <h1>图文展示</h1>

    <!-- 导航说明 -->
    <nav class="navigation-bar">
      <ul>
        <li><router-link to="/result1">全部</router-link></li>
        <li><router-link to="/result1/explain">说明</router-link></li>
        <li><router-link to="/result1/activity">活动</router-link></li>
        <li><router-link to="/result1/expansion">扩展包</router-link></li>
      </ul>
    </nav>

    <!-- 容器 -->
    <div class="image-container">
      <ul>
        <!-- 动态生成8个li -->
        <li v-for="(image, index) in images" :key="index" class="image-item">
          <div class="image-wrap">
            <img :src="image.src" alt="Image" class="image"/>
            <div class="overlay">
              <div class="title">{{ image.title }}</div>
              <div class="text">{{ image.text }}</div>
            </div>
          </div>
        </li>
      </ul>
    </div>

  </div>

</template>

<script setup>
  import { ref } from 'vue'
  const name = 'result1'

  const images = [
  { src: 'https://via.placeholder.com/1000x200', title: 'title1', text: 'Image 1' },
  { src: 'https://via.placeholder.com/1000x200', title: 'title2', text: 'Image 2' },
  { src: 'https://via.placeholder.com/1000x200', title: 'title3', text: 'Image 3' },
  { src: 'https://via.placeholder.com/1000x200', title: 'title4', text: 'Image 4' },
  { src: 'https://via.placeholder.com/1000x200', title: 'title5', text: 'Image 5' },
  { src: 'https://via.placeholder.com/1000x200', title: 'title6', text: 'Image 6' },
  { src: 'https://via.placeholder.com/1000x200', title: 'title7', text: 'Image 7' },
  { src: 'https://via.placeholder.com/1000x200', title: 'title8', text: 'Image 8' },
]

</script>

<style>

.navigation-bar {
  background-color: #f8f8f8;
  border: 1px solid #ddd;
  padding: 10px;
  margin: 10px;
  /* text-align: center; */
}

.navigation-bar ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.navigation-bar li {
  display: inline-block;
  margin-right: 10px;
}

.navigation-bar a {
  text-decoration: none;
  color: #333;
  font-weight: bold;
}

.navigation-bar a.router-link-active {
  color: #007bff;
}

/* 容器样式 */
.image-container {
  width: 100%;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 20px; /* 控制每个li之间的间隔 */
}

/* 每个li的样式 */
.image-container ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.image-item {
  position: relative;
  width: 100%;
  height: 200px; /* 固定每个图片的高度 */
  display: block;
  margin-bottom: 20px; /* 添加li之间的间隙 */
}

.image-wrap {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover; /* 使图片充满区域 */
  transition: transform 0.5s ease-in-out;
}

/* 遮罩层样式 */
.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5); 
  opacity: 0;
  transition: opacity 0.3s ease;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 10px;
}

.overlay .title {
  font-size: 30px;
  font-weight: bold;
  color: white;
  margin-bottom: 10px;
}

.overlay .text {
  font-size: 18px;
  color: white;
  text-shadow: 0 0 5px rgba(0, 0, 0, 0.7);
}

/* 鼠标悬停时的效果 */
.image-item:hover .image {
  transform: scale(1.1);
}

.image-item:hover .overlay {
  opacity: 1;
}

</style>
