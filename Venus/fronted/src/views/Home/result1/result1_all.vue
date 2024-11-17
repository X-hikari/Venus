<template>
  <!-- 容器 -->
  <div class="image-container">
    <ul>
      <!-- 动态生成8个li，使用router-link包裹每个li -->
      <router-link v-for="(image, index) in images" :key="index" :to="image.link" class="image-item">
        <li>
          <div class="image-wrap">
            <img :src="image.src" alt="Image" class="image"/>
            <div class="result1_overlay">
              <div class="title">{{ image.title }}</div>
              <div class="text">{{ image.text }}</div>
            </div>
          </div>
        </li>
      </router-link>
    </ul>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  const name = 'result1_all'

  const images = [
  { src: '/result1/images/article1.png', title: '小知识——中国法律的起源', text: '中国法律源远流长，起初以部落刑法为基础，经历夏、商、周、秦等朝代发展，最终形成完整法律体系', link: '/article/1' },
  { src: '/result1/images/article2.png', title: '小知识——如何获得法律援助', text: '法律援助为经济困难人士提供免费法律服务，保障其合法权益，申请时需提供相关材料，可拨打12348或查询法律服务网获取帮助。', link: '/article/2' },
  { src: '/result1/images/article3.jpg', title: '小知识——生活中的帮助', text: '面向特殊群体的公共服务设施包括硬性设施和人性化服务，旨在保障其出行和生活便利，但实际执行仍存在差距，需要社会关注和改善。', link: '/article/3' },
  { src: '/result1/images/article4.jpg', title: '小知识——遇到校园欺凌怎么办？', text: '校园欺凌普遍存在，影响学生身心健康。我们应通过冷静应对、求助他人、依法保护等措施应对校园暴力，共同营造和谐安全的校园环境。', link: '/article/4' },
  { src: 'https://via.placeholder.com/1000x200', title: 'title5', text: 'Image 5', link: '/article/5' },
  { src: 'https://via.placeholder.com/1000x200', title: 'title6', text: 'Image 6', link: '/article/6' },
  { src: 'https://via.placeholder.com/1000x200', title: 'title7', text: 'Image 7', link: '/article/7' },
  { src: 'https://via.placeholder.com/1000x200', title: 'title8', text: 'Image 8', link: '/article/8' },
]

</script>

<style>

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
.result1_overlay {
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

.result1_overlay .title {
  font-size: 30px;
  font-weight: bold;
  color: white;
  margin-bottom: 10px;
}

.result1_overlay .text {
  font-size: 18px;
  color: white;
  text-shadow: 0 0 5px rgba(0, 0, 0, 0.7);
}

/* 鼠标悬停时的效果 */
.image-item:hover .image {
  transform: scale(1.1);
}

.image-item:hover .result1_overlay {
  opacity: 1;
}

</style>