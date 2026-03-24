// 通用工具函数

/**
 * 格式化日期
 * @param {Date | string} date 
 * @returns {string}
 */
export function formatDate(date) {
  if (!date) return '';
  const d = new Date(date);
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')} ${String(d.getHours()).padStart(2, '0')}:${String(d.getMinutes()).padStart(2, '0')}:${String(d.getSeconds()).padStart(2, '0')}`;
}

/**
 * 检查是否有权限
 * @param {string} permission 
 * @returns {boolean}
 */
export function checkPermission(permission) {
  // 这里可以结合 store 中的权限进行检查
  return true; // 简化处理，实际项目中应从store获取
}