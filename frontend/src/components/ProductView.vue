<template>
  <md-dialog :md-active.sync="open">
      <md-dialog-title>View Product</md-dialog-title>
      <div class="md-dialog-content">
        <div class="product-details">
          <div class="product-detail">
            <label>Name:</label>
            <div class="value">{{product.name}}</div>
          </div>
          <div class="product-detail">
            <label>SKU:</label>
            <div class="value">{{product.sku}}</div>
          </div>
          <div class="product-detail">
            <label>Quantity:</label>
            <div class="value">{{product.quantity}}</div>
          </div>
        </div>
        <md-table class="stock-list">
          <md-table-toolbar>
            <h1 class="md-title">Stocks</h1>
          </md-table-toolbar>

          <md-table-row>
            <md-table-head md-numeric>Quantity</md-table-head>
            <md-table-head>Date</md-table-head>
            <md-table-head>Transaction Type</md-table-head>
          </md-table-row>

          <md-table-row 
            v-for="(stock, index) in product.stocks"
            :key="index"
          >
            <md-table-cell md-numeric>{{stock.quantity}}</md-table-cell>
            <md-table-cell>{{stock.date | moment("YYYY-MM-DD hh:mm")}}</md-table-cell>
            <md-table-cell>{{stock.transactionType ? "Stocked In" : "Stocked Out"}}</md-table-cell>
          </md-table-row>
        </md-table>
      </div>
      <md-dialog-actions>
        <md-button class="md-primary" @click="closeDialog">Close</md-button>
      </md-dialog-actions>
    </md-dialog>
</template>

<script>
export default {
  name: "ProductView",
  props: ['open', 'product'],
  methods: {
    closeDialog: function() {
      this.$emit("close-dialog", false);
    }
  }
}
</script>

<style>
  .md-dialog {
    width: 600px;
  }

  .md-dialog-content {
    max-height: 300px;
    overflow: auto;
  } 

  .product-details {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
  }

  .product-detail label {
    font-weight: bold;
    margin-bottom: 5px;
  }
</style>
