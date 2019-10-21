<template>
  <div id="app">
    <div class="forms">
      <product-form 
        v-on:add-success="successfulAdd"
      />
      <transaction-form 
        :products="products"
        v-on:add-success="successfulTransaction"
      />
    </div>
    <product-list 
      :products="products"
      v-on:view-product="openDialog"
    />
    <product-view 
      :open="openProductView"
      :product="product"
      v-on:close-dialog="closeDialog"
    />
    <md-snackbar 
      md-position="center" 
      :md-duration="4000" 
      :md-active.sync="openSnackbar" 
      md-persistent
    >
        <span>{{snackbarMessage}}</span>
        <md-button class="md-primary" @click="openSnackbar = false">Close</md-button>
    </md-snackbar>
  </div>
</template>

<script>
import Vue from 'vue';
import AddTransactionForm from "./components/AddTransactionForm";
import AddProductForm from "./components/AddProductForm";
import ProductList from "./components/ProductList";
import ProductView from "./components/ProductView";

export default {
  name: "App",
  mounted() {
    this.getProducts();
  },
  components: {
    'transaction-form': AddTransactionForm,
    'product-form': AddProductForm,
    'product-list': ProductList,
    'product-view': ProductView
  },
  data: function() {
    return {
      openProductView: false,
      openSnackbar: false,
      snackbarMessage: "",
      product: {
        "name": "Sample",
        "sku": "sample-12345",
        "quantity": 110,
        "stocks": [
              {
                  "product": 1,
                  "quantity": 10,
                  "date": "2019-10-19T10:11:00Z",
                  "transactionType": 1
              },
              {
                  "product": 1,
                  "quantity": 10,
                  "date": "2019-10-19T10:10:00Z",
                  "transactionType": 1
              },
              {
                  "product": 1,
                  "quantity": 10,
                  "date": "2019-10-19T10:09:00Z",
                  "transactionType": 1
              },
              {
                  "product": 1,
                  "quantity": 10,
                  "date": "2019-10-19T10:08:00Z",
                  "transactionType": 1
              },
              {
                  "product": 1,
                  "quantity": 10,
                  "date": "2019-10-19T10:07:00Z",
                  "transactionType": 1
              },
              {
                  "product": 1,
                  "quantity": 10,
                  "date": "2019-10-19T10:06:00Z",
                  "transactionType": 1
              },
              {
                  "product": 1,
                  "quantity": 10,
                  "date": "2019-10-19T10:05:00Z",
                  "transactionType": 1
              },
              {
                  "product": 1,
                  "quantity": 10,
                  "date": "2019-10-19T10:04:00Z",
                  "transactionType": 1
              },
              {
                  "product": 1,
                  "quantity": 10,
                  "date": "2019-10-19T10:03:00Z",
                  "transactionType": 1
              },
              {
                  "product": 1,
                  "quantity": 10,
                  "date": "2019-10-19T10:02:00Z",
                  "transactionType": 1
              }
          ]
      },
      products: [],
    }
  }, 
  methods: {
    getProducts: function() {
      Vue.axios.get("http://localhost:8000/product/").then((response) => {
        this.products = response.data;
      })
    },
    successfulAdd: function() {
      this.snackbarMessage = "Item successfully added.";
      this.openSnackbar = true;
      this.getProducts();
    },
    successfulTransaction: function() {
      this.snackbarMessage = "Transaction Successful.";
      this.openSnackbar = true;
      this.getProducts();
    },
    closeDialog: function(status) {
      this.openProductView = status;
    },
    openDialog: function(index) {
      this.openProductView = true;
      this.product = this.products[index];
    }
  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  display: grid;
  grid-template-columns: 1fr 2fr;
  grid-gap: 15px;
  max-width: 1000px;
  margin: 60px auto;
  align-items: flex-start;
}

html, body {
  background-color: #efefef !important;
  height: 100%;
}

body {
  margin: 0 15px;
}

.md-card {
  background-color: #ffffff;
}
</style>
