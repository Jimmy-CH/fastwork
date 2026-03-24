<!-- src/layouts/Layout.vue -->
<template>
  <el-container class="layout-container">
    <!-- 侧边栏 -->
    <el-aside :width="sidebarWidth">
      <Sidebar :is-collapse="isCollapse" />
    </el-aside>

    <el-container>
      <!-- 头部 -->
      <el-header>
        <Header @toggle-collapse="handleToggleCollapse" :is-collapse="isCollapse" />
      </el-header>

      <!-- 主内容区 -->
      <el-main>
        <RouterView />
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup>
import { ref, computed } from 'vue';
import Sidebar from '@/components/Layout/Sidebar.vue';
import Header from '@/components/Layout/Header.vue';

const isCollapse = ref(false);

// 计算属性，根据 isCollapse 返回不同的宽度
const sidebarWidth = computed(() => isCollapse.value ? '64px' : '240px');

// 处理来自 Header 的折叠切换事件
const handleToggleCollapse = () => {
  isCollapse.value = !isCollapse.value;
};
</script>

<style scoped>
.layout-container {
  height: 100vh;
}

.el-header {
  border-bottom: 1px solid #d8dce5;
  background-color: white;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  box-sizing: border-box;
}

.el-aside {
  background-color: var(--el-bg-color-overlay);
  color: var(--el-text-color-primary);
  transition: width 0.3s; /* 为宽度变化添加过渡效果 */
}

.el-main {
  background-color: #f0f2f5;
  padding: 20px;
}
</style>