<!-- src/views/Dashboard.vue -->
<template>
  <div class="dashboard">
    <h2>欢迎使用 FastWork 系统</h2>
    <p>这里是系统的仪表盘，您可以快速查看关键指标。</p>

    <!-- 使用 Collapse 组件包裹统计卡片区域 -->
    <el-collapse v-model="activeNames" accordion>
      <el-collapse-item title="系统数据概览" name="1">
        <el-row :gutter="20" style="margin-top: 20px;">
          <el-col :span="6">
            <el-card shadow="hover">
              <div class="stat-card">
                <h3>100+</h3>
                <p>总客户数</p>
              </div>
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card shadow="hover">
              <div class="stat-card">
                <h3>500+</h3>
                <p>总工单数</p>
              </div>
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card shadow="hover">
              <div class="stat-card">
                <h3>200+</h3>
                <p>产品总数</p>
              </div>
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card shadow="hover">
              <div class="stat-card">
                <h3>98%</h3>
                <p>满意度</p>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-collapse-item>
    </el-collapse>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// 定义响应式数据，用于控制哪个面板是展开的
// accordion: true 表示手风琴模式，一次只能打开一个
const activeNames = ref(['1']); // 初始状态展开第一个面板
</script>

<style scoped>
.dashboard {
  padding: 20px;
}

.stat-card {
  text-align: center;
}

.stat-card h3 {
  margin: 0;
  color: #409EFF;
}

.stat-card p {
  margin: 10px 0 0 0;
  color: #909399;
}

/* 可选：调整 collapse 内边距，使布局更美观 */
.el-collapse-item__content {
  padding-bottom: 0;
}
</style>