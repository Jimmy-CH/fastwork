<!-- src/views/Dashboard.vue -->
<template>
  <div class="dashboard">
    <h2>欢迎使用 FastWork 系统</h2>
    <p>这里是系统的仪表盘，您可以快速查看关键指标。</p>
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
  </div>
</template>

<script setup>
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
</style>