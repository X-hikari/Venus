<template>
  <div class="article">
    <h1>{{ article.title || '加载中...' }}</h1>
    <div v-html="convertedContent || '内容加载失败或为空，请稍后再试。'"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router'; // 导入 useRoute 来访问路由
import axios from 'axios';
import { marked } from 'marked'

const article = ref({});  // 存储文章数据
const convertedContent = ref('');  // 存储转换后的 HTML 内容

// 获取文章内容
const fetchArticle = async (id) => {
  try {
    const response = await axios.get(`http://localhost:8001/api/article/${id}/`);
    console.log('Article data:', response.data);  // 打印返回的数据，确认结构
    article.value = response.data;  // 保存文章数据
    convertMarkdownToHtml(article.value.content);  // 转换 Markdown 内容
  } catch (error) {
    console.error('Error fetching article:', error);
  }
};

// 将 Markdown 转换为 HTML
const convertMarkdownToHtml = (markdownContent) => {
  if (markdownContent) {
    convertedContent.value = marked(markdownContent);  // 将 Markdown 转换为 HTML
    console.log('Converted content:', convertedContent.value); // 打印转换后的 HTML 内容
  } else {
    console.error('No content found to convert!');
  }
};

// 使用 useRoute 获取路由参数
const route = useRoute();
const articleId = route.params.id;  // 获取 URL 中的动态参数 id

// 组件挂载时执行
onMounted(() => {
  fetchArticle(articleId);  // 使用从路由获取的 articleId 获取文章
});
</script>

<style scoped>
/* 根据需要添加样式 */
.article {
  padding: 20px;
  font-family: Arial, sans-serif;
}

h1 {
  font-size: 2rem;
  color: #333;
}

div[v-html] {
  margin-top: 20px;
  font-size: 1.1rem;
  color: #555;
}
</style>
