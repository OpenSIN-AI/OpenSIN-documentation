<script setup>
defineProps({
  name: {
    type: String,
    required: true,
  },
  variant: {
    type: String,
    default: 'latest',
  },
})
</script>

<template>
  <span :class="['oa-card-icon', `oa-card-icon--${variant}`]" aria-hidden="true">
    <svg v-if="name === 'book'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
      <path d="M4.5 6.5A2.5 2.5 0 0 1 7 4h12.5v14H7a2.5 2.5 0 0 0-2.5 2.5z" />
      <path d="M7 4v16" />
      <path d="M10 8h7" />
      <path d="M10 12h7" />
    </svg>

    <svg v-else-if="name === 'chat'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
      <path d="M6 6.5h12a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2H11l-4.5 3v-3H6a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2Z" />
      <path d="M8 10h8" />
      <path d="M8 13h5" />
    </svg>

    <svg v-else-if="name === 'terminal'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
      <path d="M4.5 6.5h15v11h-15z" />
      <path d="m8 10 2.5 2.5L8 15" />
      <path d="M13.5 15h3" />
    </svg>

    <svg v-else-if="name === 'monitor'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
      <rect x="4.5" y="5.5" width="15" height="10" rx="1.8" />
      <path d="M9 18.5h6" />
      <path d="M12 15.5v3" />
    </svg>

    <svg v-else-if="name === 'search'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
      <circle cx="10.5" cy="10.5" r="4.8" />
      <path d="m14.2 14.2 4 4" />
      <path d="M8.5 8.5h4" />
      <path d="M8.5 12h2.8" />
    </svg>

    <svg v-else-if="name === 'image'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
      <rect x="4.5" y="5.5" width="15" height="13" rx="1.8" />
      <circle cx="9" cy="10" r="1.2" fill="currentColor" stroke="none" />
      <path d="M6.2 16 10 12.2l2.2 2.2 1.8-1.8 3.8 3.4" />
    </svg>

    <svg v-else-if="name === 'spark'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
      <path d="M12 4.5l1.5 4.2L18 10.2l-4.5 1.5L12 16l-1.5-4.3L6 10.2l4.5-1.5L12 4.5Z" />
      <path d="M18.5 4.5l.6 1.7 1.7.6-1.7.6-.6 1.7-.6-1.7-1.7-.6 1.7-.6.6-1.7Z" />
    </svg>

    <svg v-else-if="name === 'gift'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
      <rect x="4.5" y="9" width="15" height="9" rx="1.6" />
      <path d="M4.5 12h15" />
      <path d="M12 9v9" />
      <path d="M10.5 9c-1.5 0-3-1-3-2.5S9 4 10.5 5.5 12 9 12 9s.5-3.5 3-3.5S19 5.5 19 6.5s-1.5 2.5-3 2.5" />
    </svg>

    <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
      <path d="M12 4.5l2.3 4.7 5.2.8-3.7 3.5.9 5.2-4.7-2.5-4.7 2.5.9-5.2-3.7-3.5 5.2-.8z" />
    </svg>
  </span>
</template>

<style scoped>
.oa-card-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: currentColor;
}

.oa-card-icon svg {
  display: block;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.oa-card-icon--latest {
  width: 30px;
  height: 30px;
  color: #ffffff;
}

.oa-card-icon--latest svg {
  width: 18px;
  height: 18px;
}

.oa-card-icon--explore {
  width: 58px;
  height: 58px;
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.95);
  color: #111827;
  box-shadow: 0 10px 24px rgba(15, 23, 42, 0.12);
}

.oa-card-icon--explore svg {
  width: 24px;
  height: 24px;
}
</style>
