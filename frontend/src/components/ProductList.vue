<template>
    <md-table class="product-list md-card">
      <md-table-toolbar>
        <h1 class="md-title">Products</h1>
      </md-table-toolbar>

      <md-table-row>
        <md-table-head>Name</md-table-head>
        <md-table-head>SKU</md-table-head>
        <md-table-head md-numeric>Quantity</md-table-head>
        <md-table-head class="md-center">Action</md-table-head>
      </md-table-row>

      <md-table-row 
        v-for="(product, index) in products"
        :key="index"
      >
        <md-table-cell>{{product.name}}</md-table-cell>
        <md-table-cell>{{product.sku}}</md-table-cell>
        <md-table-cell md-numeric>{{product.quantity}}</md-table-cell>
        <md-table-cell class="md-center">
          <md-button 
            class="md-primary"
          >
            View
          </md-button>
        </md-table-cell>
      </md-table-row>
    </md-table>
</template>

<script>

export default {
  name: "ProductList",
  props: ['products'],
}
</script>

<style>
  .md-title {
    text-align: left;
  }

  .product-list {
    display: flex;
    margin: 0;
  }
  .product {
    margin: 10px 12px;
  }

  .md-table-cell {
    text-align: left;
  }

  .md-center {
    text-align: center;
  }

  .md-table-cell.md-numeric {
    text-align: right;
  }
</style>
