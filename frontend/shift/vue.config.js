const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000', // 実際のバックエンドサーバーのURL
        changeOrigin: true, // オリジンヘッダーの書き換え
        pathRewrite: {
          '^/api': '' // URLの書き換えルール
        }
      }
    }
  },
  transpileDependencies: true,
  pluginOptions: {
    vuetify: {
			// https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
		}
  }
})
