<template>
  <div>

    <!-- 主体内容，左右分栏 -->
    <div class="main-content">
      <!-- 左侧轮播图 -->
      <div class="carousel-container">
        <div class="carousel">
          <img :src="images[currentImage]" alt="Carousel Image" class="carousel-image" />
          <!-- 图片指示器 -->
          <div class="carousel-indicators">
            <div
              v-for="(image, index) in images"
              :key="index"
              :class="['indicator-dot', { active: index === currentImage }]"
              @click="goToImage(index)"
            ></div>
          </div>
          <button @click="prevImage" class="carousel-button left"> < </button>
          <button @click="nextImage" class="carousel-button right"> > </button>
        </div>
      </div>

      <!-- 右侧内容区域 -->
      <div class="right-content  boxed-item">
        <!-- 标题和更多链接 -->
        <div class="header-section">
          <h2>索引标题</h2>
          <a href="#more" class="more-link">更多</a>
        </div>

        <!-- 分隔线 -->
        <div class="separator"></div>

        <!-- 链接列表 -->
        <ul class="link-list">
          <li><a href="#item1">这是第一项链接</a></li>
          <li><a href="#item2">这是第二项链接</a></li>
          <li><a href="#item3">这是第三项链接</a></li>
          <li><a href="#item4">这是第四项链接</a></li>
          <li><a href="#item5">这是第五项链接</a></li>
          <li><a href="#item6">这是第六项链接</a></li>
          <li><a href="#item7">这是第七项链接</a></li>
          <li><a href="#item8">这是第八项链接</a></li>
          <li><a href="#item9">这是第九项链接</a></li>
          <li><a href="#item10">这是第十项链接</a></li>
        </ul>
      </div>
    </div>

    <!-- 成果展示 -->
    <div class="results">
      <!-- 上部分：标题 -->
      <div class="results-title">
        <h2>成果展示</h2>
      </div>

      <!-- 下部分：均分成四个部分，每个部分放一张图片 -->
      <div class="results-gallery">
        <div class="result-item">
          <router-link to="/result1">
            <img src="../assets/result1.jpg" alt="成果图1" />
            <div class="overlay">
              <div class="overlay-text">成果 1</div>
            </div>
          </router-link>
        </div>
        <div class="result-item">
          <a href="#result2">
            <img src="../assets/result2.jpg" alt="成果图2" />
            <div class="overlay">
              <div class="overlay-text">成果 2</div>
            </div>
          </a>
        </div>
        <div class="result-item">
          <a href="#result3">
            <img src="../assets/result3.jpg" alt="成果图3" />
            <div class="overlay">
              <div class="overlay-text">成果 3</div>
            </div>
          </a>
        </div>
        <div class="result-item">
          <a href="#result4">
            <img src="../assets/result4.jpg" alt="成果图4" />
            <div class="overlay">
              <div class="overlay-text">成果 4</div>
            </div>
          </a>
        </div>
      </div>
    </div>

  </div>
  
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

// 轮播图图片列表
const images = [
  './footer.jpg',
  './header.jpg',
  './logo.png',
]

const currentImage = ref(0)

function nextImage() {
  currentImage.value = (currentImage.value + 1) % images.length
}

function prevImage() {
  currentImage.value = (currentImage.value - 1 + images.length) % images.length
}

function goToImage(index) {
  currentImage.value = index
}

// 定时器变量
let autoSwitchInterval = null

// 在组件挂载时启动定时器
onMounted(() => {
  autoSwitchInterval = setInterval(() => {
    nextImage()  // 每3秒切换图片
  }, 3000)
})

// 在组件卸载时清除定时器
onBeforeUnmount(() => {
  if (autoSwitchInterval) {
    clearInterval(autoSwitchInterval)
  }
})

const name = 'Home'

</script>

<style scoped>
/* 主体内容区域样式 */
.main-content {
  display: flex;
  justify-content: space-between;
  height: 430px;
}

.carousel-container {
  position: relative;
  left: 0;
  width: 50vw;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  box-sizing: border-box; /* 避免padding影响布局宽度 */
}

.carousel {
  position: relative;
  width: 100%;
  height: 100%;
}

.carousel-image {
  width: 100%;
  height: 100%; /* 固定宽度 */
  object-fit: cover; /* 裁剪图片以填满指定区域 */
  border-radius: 8px;
}

/* 左右按钮样式 */
.carousel-button {
  width: 40px;
  height: 40px;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  padding: 10px;
  cursor: pointer;
  font-size: 16px;
  border-radius: 50%; /* 设置为圆形 */
}

.carousel-button.left {
  left: 10px;
}

.carousel-button.right {
  right: 10px;
}

.carousel-button:hover {
  background-color: rgba(0, 0, 0, 0.7);
}

/* 图片指示器容器 */
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  right: 20px;
  display: flex;
  gap: 8px;
}

/* 小点样式 */
.indicator-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.5);
  transition: background-color 0.3s;
  cursor: pointer;
}

.indicator-dot:hover {
  background-color: rgba(0, 0, 0, 0.5);
}

.indicator-dot.active {
  background-color: rgba(255, 255, 255, 0.9);
}

.right-content {
  margin: 20px;
  width: 50%;
  height: 260; /* 确保高度填充整个可用区域 */
  padding: 0px;
  border: 2px solid black; /* 添加外框 */
  border-radius: 10px; /* 圆角效果 */
  box-sizing: border-box; /* 确保外框不影响布局 */
  display: flex;
  flex-direction: column;
}

/* 标题和更多链接的布局 */
.header-section {
  display: flex;
  justify-content: space-between; /* 将标题和更多链接分开 */
  align-items: center;
  margin-bottom: 10px;
}

.header-section h2 {
  font-size: 24px;
  font-weight: bold;
  padding-top: 10px;
  padding-left: 10px;
}

.more-link {
  color: black; 
  text-decoration: none;
  font-size: 16px;
  padding-top: 10px;
  padding-right: 10px;
}

.more-link:hover {
  text-decoration: underline; /* 鼠标悬停时显示下划线 */
}

/* 添加分隔线 */
.separator {
  border-bottom: 2px solid grey; /* 蓝色分隔线 */
  margin: 0px 20px 5px 20px; /* 上下留空隙，左右留空隙 */
  padding-bottom: 5px; /* 使分隔线与内容之间留出空间 */
}

/* 链接列表样式 */
.link-list {
  list-style-type: none;
  padding: 0;
}

.link-list li {
  margin: 5px 0;
  position: relative; /* 为小圆点定位 */
  padding-left: 35px; /* 给小圆点留出空间 */
}

.link-list li::before {
  padding-left: 15px;
  content: '•'; /* 添加小圆点 */
  font-size: 20px;
  color: black; /* 设置小圆点的颜色 */
  position: absolute;
  left: 0; /* 将小圆点定位到左侧 */
  top: 50%;
  transform: translateY(-50%); /* 垂直居中小圆点 */
}

.link-list a {
  color: black; /* 链接颜色 */
  text-decoration: none;
  font-size: 16px;
}

.link-list a:hover {
  color: blue; /* 链接颜色 */
  text-decoration: underline; /* 鼠标悬停时加下划线 */
}

/* 成果展示部分样式 */
.results {
  margin-top: 30px; /* 添加顶部间距 */
  padding: 20px;
}

.results-title h2 {
  font-size: 28px;
  font-weight: bold;
  /* text-align: center; */
  margin-bottom: 20px; /* 标题下方的间距 */
}

.results-gallery {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* 四列布局 */
  gap: 20px; /* 每列之间的间距 */
}

.result-item {
  position: relative;
  height: 200px; /* 固定每个部分的高度 */
  overflow: hidden;
  border-radius: 8px; /* 图片边角圆滑 */
}

.result-item img {
  width: 100%;
  height: 100%;
  object-fit: cover; /* 图片裁剪填满每个区域 */
}

.result-item a {
  display: block; /* 让链接占满整个图片区域 */
  width: 100%;
  height: 100%;
  position: relative;
}

/* 遮罩层样式 */
.overlay {
  position: absolute;
  bottom: -100%; /* 初始状态：隐藏在图片底部 */
  left: 0;
  width: 100%;
  height: 80%;
  background-color: rgba(0, 0, 0, 0.6); /* 半透明黑色背景 */
  display: flex;
  justify-content: center;
  align-items: center;
  transition: bottom 0.5s ease; /* 平滑的过渡效果 */
}

/* 鼠标悬停时遮罩层从下方滑出 */
.result-item:hover .overlay {
  bottom: 0; /* 鼠标移上去时，遮罩层滑上来 */
}

/* 遮罩层中的文字样式 */
.overlay-text {
  color: white;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  padding: 10px;
}

</style>
