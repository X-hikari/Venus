<template>
  <div id="app">

    <!-- 顶部图片区域 -->
    <div class="top-banner">
      <img src="./src/assets/header.jpg" alt="Banner" class="banner-image" />
      <div class="banner-text">童心启航，法制相随——普法网</div>
    </div>

    <!-- 导航栏 -->
    <nav class="navbar">
      <ul>
        <li><router-link to="/home">首页</router-link></li>
        <li><router-link to="/news">最新动态</router-link></li>
        <li><router-link to="/about">关于我们</router-link></li>
      </ul>
    </nav>

    <div class="static">
        <router-view></router-view>
    </div>

    <!-- 页脚部分 -->
    <footer class="footer">
      <div class="footer-content">
        <p>&copy; 2024 Venus. 版权所有.</p>
        <div class="social-links">
          <a href="https://github.com/xxywindy/Venus" target="_blank">GitHub</a> | 
          <a href="https://example.com" target="_blank">LinkedIn</a> | 
          <a href="mailto:3220100037@zju.edu.cn">Email</a>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
  
</script>

<style scoped>
/* 设置页面整体布局 */
.app {
  display: flex;
  margin: 0;
  padding: 0;
  align-items: flex-start; /* 确保内容从顶部开始 */
  flex-direction: column; /* 设置主轴为竖向 */
  height: 100vh; /* 使整个页面的高度占满视口 */
}

/* 顶部图片区域样式 */
.top-banner {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100px;
  overflow: hidden;
  z-index: 1000; /* 确保顶层显示 */
}

.banner-image {
  width: 100%;
  height: 100%;
  object-fit: cover; /* 保持图片宽高比，填充整个区域 */
}

/* 文字叠加样式 */
.banner-text {
  position: absolute;
  top: 50%;
  left: 35%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 26px;
  font-weight: bold;
  text-shadow: 0px 0px 5px rgba(0, 0, 0, 0.7); /* 添加阴影提升文字可读性 */
}

/* 导航栏样式 */
.navbar {
  position: fixed;
  top: 100px; /* 紧贴在图片下方 */
  left: 0;
  width: 100%;
  background-color: #333;
  color: white;
  z-index: 999;
}

.navbar ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
}

.navbar li {
  margin: 0 15px;
}

.navbar a {
  color: white;
  text-decoration: none;
  font-size: 16px;
}

.navbar a:hover {
  text-decoration: underline;
}

/* 页脚部分样式 */
.footer {
  background-color: #333;
  color: white;
  padding: 20px;
  text-align: center;
  /* position: relative; */
  bottom: 0;
  width: 1200px;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
}

.footer p {
  font-size: 14px;
  margin-bottom: 10px;
}

.social-links a {
  color: #ffffff;
  text-decoration: none;
  margin: 0 10px;
}

.social-links a:hover {
  text-decoration: underline;
}

/* 确保页面内容不被顶部固定的图片遮挡 */
.static {
  padding-top: 130px; /* 留出顶部空间 */
  margin: 0;
}

</style>