<template>
  <form class="md-card product-form" @submit="submitForm">
    <md-card-header>
        <h1 class="md-title">Add Product</h1>
    </md-card-header>
    <md-field>
      <label>Name</label>
      <md-input v-model="name"></md-input>
    </md-field>
    <md-field>
      <label>SKU</label>
      <md-input v-model="sku"></md-input>
    </md-field>
    <md-card-actions>
      <md-button type="submit" class="md-primary">Submit</md-button>
    </md-card-actions>
  </form>
</template>

<script>
export default {
  name: "ProductForm",
  data: function() {
    return {
      name: "",
      sku: "",
    }
  },
  methods: {
    submitForm(event) {
      event.preventDefault();
    }
  }
}
</script>

<style>
  .product-form {
    padding: 0px 20px;
    margin-bottom: 15px;
  }
</style>
