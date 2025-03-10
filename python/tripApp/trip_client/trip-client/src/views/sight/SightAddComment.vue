<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'//用于控制页面跳转工具
import { ajax } from '@/utils/ajax'//用于发送请求的工具
import { SightApis } from '@/utils/apis';
import { showToast } from 'vant';
import axios from 'axios';
import { nextTick } from 'vue';

const route = useRoute()//获取路由参数
const router = useRouter()//获取路由实例
const message = ref('')
const rate = ref(0)
const commentTextarea = ref(null) // 定义一个 ref 来存储对 textarea 的引用

const tags = ['赞', '好评', '差评', '推荐', '一般'];

const insertTag = (tag) => {
  if (commentTextarea.value) {
    const textarea = commentTextarea.value.$el.querySelector('textarea'); // 确保获取的是内部的 textarea 元素
    const startPos = textarea.selectionStart;
    const endPos = textarea.selectionEnd;
    const beforeText = message.value.substring(0, startPos);
    const afterText = message.value.substring(endPos);
    message.value = beforeText + tag + afterText;

    // 使用 nextTick 等待 DOM 更新
    nextTick(() => {
      textarea.focus();
      // 重新设置光标位置在插入的标签文本之后
      textarea.setSelectionRange(startPos + tag.length, startPos + tag.length);
    });
  }
};

const goBack = () => {
  router.push({ name: 'SightDetail', params: { id: route.params.id } });
}

const submitComment = async () => {
  console.log('submitComment 被触发');  // 确认函数是否被调用

  // 检查评论内容是否为空
  if (!message.value.trim()) {
    showToast('评论内容不能为空');
    return;
  }

  // 检查 route.params.id 是否有效
  console.log('route.params.id:', route.params.id);
  if (!route.params.id) {
    showToast('评论失败，ID 无效');
    return;
  }

  // 替换 URL 中的 #{id} 占位符
  const apiUrl = SightApis.addCommentUrl.replace('#{id}', route.params.id);
  console.log('最终请求的 API URL:', apiUrl);

  // 准备 FormData
  const formData = new FormData();
  formData.append('content', message.value.trim());  // 添加评论内容
  formData.append('score', rate.value);  // 添加评分

  // 如果有图片，处理图片上传
  if (fileList.value && fileList.value.length > 0) {
    fileList.value.forEach(file => {
      formData.append('images', file);
    });
  }

  try {
    // 调用后端 API 保存评论
    const response = await axios.post(apiUrl, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',  // 注意：这里需要 multipart/form-data 处理文件上传
      }
    });

    console.log('响应结果:', response);

    // 根据返回的数据处理
    if (response.data.success) {
      showToast('评论发布成功');
      router.go();  // 评论成功后返回上一页
    } else {
      showToast(response.data.message || '发布失败');
    }
  } catch (error) {
    console.log('错误信息:', error);
    showToast('网络异常，请稍后再试');
  }
};


// 上传图片设计
const fileList = ref([
  { url: 'https://fastly.jsdelivr.net/npm/@vant/assets/leaf.jpeg' },
  // Uploader 根据文件后缀来判断是否为图片文件
  // 如果图片 URL 中不包含类型信息，可以添加 isImage 标记来声明
  //   { url: 'https://cloud-image', isImage: true },
  { url: 'https://fastly.jsdelivr.net/npm/@vant/assets/leaf.jpeg' },
  { url: 'https://fastly.jsdelivr.net/npm/@vant/assets/leaf.jpeg' },
  { url: 'https://fastly.jsdelivr.net/npm/@vant/assets/leaf.jpeg' },
  { url: 'https://fastly.jsdelivr.net/npm/@vant/assets/leaf.jpeg' },
  { url: 'https://fastly.jsdelivr.net/npm/@vant/assets/leaf.jpeg' },
  { url: 'https://fastly.jsdelivr.net/npm/@vant/assets/leaf.jpeg' },
  { url: 'https://fastly.jsdelivr.net/npm/@vant/assets/leaf.jpeg' },
]);

// 当图片被添加到 fileList 时触发
const onAdd = (file) => {
  if (fileList.value.length < 9) {
    fileList.value.push(file);
  } else {
    // 如果已经达到最大数量，可以显示一个提示
    showToast('最多只能添加 9 张照片');
  }
};


// 底部提示框展示
const tipshow = ref(false);
const actions = [
  { name: '继续编辑' },
  { name: '残忍离开' },
];
// 处理按钮事件
// 处理按钮选择事件
// 显示 action-sheet
const showActionSheet = () => {
  tipshow.value = true;  // 设置为 true 显示 action-sheet
};

// 处理点击操作
const handleActionSelect = (action) => {
  if (action.name === '残忍离开') {
    // showToast('你选择了 "残忍离开"');
    goBack(); // 执行返回上一页的操作
  } else if (action.name === '继续编辑') {
    // showToast('你选择了 "继续编辑"');
  }
  tipshow.value = false; // 关闭底部提示框
}

</script>
<template>
  <!-- !-- 导航栏 -->
  <div>
    <van-nav-bar left-text="返回" title="景点评论" left-arrow @click-left="showActionSheet"></van-nav-bar>
  </div>
  <!-- 评论内容 -->
  <div class="commment-content">
    <!-- 图片上传 -->
    <div class="commment-images">
      <van-uploader class="image-btn" v-model="fileList" :preview-size="[100, 100]" multiple :max-count="9"
        @add="onAdd" />
    </div>

    <!-- 文字输入 -->
    <div>
      <!-- 可以使用 CellGroup 作为容器 -->
      <van-cell-group inset>
        <van-field v-model="message" ref="commentTextarea" rows="2" type="textarea" maxlength="200"
          placeholder="分享景色、设施、交通等方面的体验，更能帮助到大家哦~ 也可以直接点击下面的标签进行快速评价哦~" show-word-limit label-align="top"
          class="commment-text" />
      </van-cell-group>
    </div>

    <!-- 标签列表 -->
    <div class="tags-container">
      <!-- <span></span> -->
      <button v-for="(tag, index) in tags" :key="index" @click="insertTag(tag)" class="tag-button">
        {{ tag }}
      </button>
    </div>

    <!-- 评分 -->
    <div>
      <van-config-provider>
        <van-form class="commment-rate">
          <van-field name="rate" label="评分">
            <template #input>
              <van-rate v-model="rate" />
            </template>
          </van-field>
          <div style="margin: 16px">
            <van-button round block type="primary" @click="submitComment" native-type="submit">
              发布
            </van-button>
          </div>
        </van-form>
      </van-config-provider>
    </div>



    <!-- 底部提示 -->
    <div>
      <van-action-sheet v-model:show="tipshow" :actions="actions" description="已经分享了这么多，真的要离开吗？" close-on-click-action
        @select="handleActionSelect" />
    </div>



  </div>


</template>

<style scoped>
/* 导航栏样式 */
.van-nav-bar {
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* 评论内容区域样式 */
.commment-content {
  padding: 16px;
}

/* 图片上传区域样式 */
.commment-images {
  margin-bottom: 16px;
}

.image-btn .van-uploader__upload {
  width: 100px;
  height: 100px;
  margin-right: 8px;
  border: 1px dashed #e5e5e5;
  border-radius: 4px;
  background-color: #f8f8f8;
}

/* 文字输入区域样式 */
.commment-text {
  margin-bottom: 16px;
  width: 100%;

}

/* 标签列表样式 */
.tags-container {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 16px;
}

.tag-button {
  padding: 4px 8px;
  border-radius: 4px;
  border: 1px solid #e5e5e5;
  background-color: #f8f8f8;
  color: #333;
  cursor: pointer;
}

.tag-button:hover {
  background-color: #e5e5e5;
}

/* 评分区域样式 */
.commment-rate {
  margin-bottom: 16px;
}

/* 底部提示框样式 */
.van-action-sheet__header {
  padding: 16px;
  background-color: #fff;
  border-bottom: 1px solid #e5e5e5;
}

.van-action-sheet__description {
  color: #666;
}

.van-action-sheet__cancel-text {
  color: #333;
}

.van-action-sheet__action {
  color: #333;
}
</style>