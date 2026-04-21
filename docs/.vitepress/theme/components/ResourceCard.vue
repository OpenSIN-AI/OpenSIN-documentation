<script setup>
defineProps({
  title: String,
  description: String,
  link: String,
  imageClass: String,
  meta: String,
  icon: Object // Optional SVG component
})
</script>

<template>
  <a :href="link" class="resource-card">
    <div :class="['card-thumb', imageClass]">
      <component v-if="icon" :is="icon" class="card-icon" />
      <slot name="image"></slot>
    </div>
    <div class="card-content">
      <h3 class="card-title">{{ title }}</h3>
      <p class="card-desc">{{ description }}</p>
      <div class="card-footer">
        <span class="card-meta" v-if="meta">{{ meta }}</span>
        <span class="card-arrow">→</span>
      </div>
    </div>
  </a>
</template>

<style scoped>
.resource-card {
  display: flex;
  flex-direction: column;
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  text-decoration: none;
  color: inherit;
  height: 100%;
}

.resource-card:hover {
  transform: translateY(-4px);
  border-color: #00cc88;
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.06), 0 4px 8px rgba(0, 204, 136, 0.04);
}

.card-thumb {
  height: 160px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f9fafb;
  position: relative;
  overflow: hidden;
}

.card-icon {
  width: 48px;
  height: 48px;
  color: #111827;
  opacity: 0.8;
}

.card-content {
  padding: 24px;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.card-title {
  margin: 0 0 8px 0;
  font-size: 1.125rem;
  font-weight: 600;
  color: #111827;
  line-height: 1.4;
}

.card-desc {
  margin: 0 0 20px 0;
  font-size: 0.9375rem;
  color: #4b5563;
  line-height: 1.6;
  flex: 1;
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 16px;
  border-top: 1px solid #f3f4f6;
}

.card-meta {
  font-size: 0.75rem;
  font-weight: 500;
  color: #9ca3af;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.card-arrow {
  font-size: 1.125rem;
  color: #111827;
  transition: transform 0.2s ease;
}

.resource-card:hover .card-arrow {
  transform: translateX(4px);
  color: #00cc88;
}

/* Gradients for OpenSIN */
.bg-sin-green { background: linear-gradient(135deg, #008060 0%, #00cc88 100%); color: white; }
.bg-sin-blue { background: linear-gradient(135deg, #00cc88 0%, #8ec5fc 100%); }
.bg-sin-orange { background: linear-gradient(135deg, #008060 0%, #00ffaa 100%); }
</style>
