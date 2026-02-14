const API_BASE = 'https://your-vercel-domain.vercel.app'

Page({
  data: {
    dream: '',
    result: false,
    analysis: '',
    loading: false
  },

  onInput: function (e) {
    this.setData({
      dream: e.detail.value
    })
  },

  analyze: function () {
    const dream = this.data.dream.trim()
    
    if (!dream) {
      wx.showToast({
        title: '请输入梦境内容',
        icon: 'none',
        duration: 2000
      })
      return
    }

    if (dream.length > 500) {
      wx.showToast({
        title: '梦境内容不能超过500字',
        icon: 'none',
        duration: 2000
      })
      return
    }

    this.setData({
      loading: true
    })

    wx.request({
      url: `${API_BASE}/analyze`,
      method: 'POST',
      data: {
        dream: dream
      },
      header: {
        'content-type': 'application/json'
      },
      success: (res) => {
        if (res.data.status === 'success') {
          this.setData({
            result: true,
            analysis: res.data.analysis
          })
        } else {
          wx.showToast({
            title: res.data.message || '解梦失败',
            icon: 'none',
            duration: 2000
          })
        }
      },
      fail: (err) => {
        wx.showToast({
          title: '网络请求失败',
          icon: 'none',
          duration: 2000
        })
        console.error('请求失败:', err)
      },
      complete: () => {
        this.setData({
          loading: false
        })
      }
    })
  },

  reset: function () {
    this.setData({
      dream: '',
      result: false,
      analysis: '',
      loading: false
    })
  },

  onShareAppMessage: function () {
    return {
      title: '🌙 AI解梦大师 - 用心理学解析你的梦境',
      path: '/pages/index/index',
      imageUrl: ''
    }
  }
})
