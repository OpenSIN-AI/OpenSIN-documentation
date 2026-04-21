import DefaultTheme from 'vitepress/theme'
import HomeChoosePath from './components/HomeChoosePath.vue'
import HomeRelatedTopics from './components/HomeRelatedTopics.vue'
import './custom.css'

export default {
  ...DefaultTheme,
  enhanceApp({ app }) {
    /**
     * Keep homepage layout primitives registered at the theme layer.
     * The homepage contract intentionally stays VitePress-native: markdown owns
     * the structure, while Vue components provide the protected 2-card and
     * 4-card sections without falling back to raw HTML blobs in docs/index.md.
     */
    app.component('HomeChoosePath', HomeChoosePath)
    app.component('HomeRelatedTopics', HomeRelatedTopics)
  },
}
