<template>
  <div id="app">
    <div class="forms">
      <product-form />
      <transaction-form 
        :products="products"
      />
    </div>
    <product-list 
      :products="products"
    />
  </div>
</template>

<script>
import Vue from 'vue';
import AddTransactionForm from "./components/AddTransactionForm";
import AddProductForm from "./components/AddProductForm";
import ProductList from "./components/ProductList";

export default {
  name: "App",
  mounted() {
    this.getProducts();
  },
  components: {
    'transaction-form': AddTransactionForm,
    'product-form': AddProductForm,
    'product-list': ProductList,
  },
  data: function() {
    return {
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
      products: []
    }
  }, methods: {
    getProducts: function() {
      Vue.axios.get("http://localhost:8000/product/").then((response) => {
        this.products = response.data;
      })
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
  align-items: baseline;
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
