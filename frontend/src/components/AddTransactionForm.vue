<template>
  <form class="md-card product-form">
    <md-card-header>
      <h1 class="md-title">Add Transaction</h1>
    </md-card-header>

    <md-field>
      <label>Product</label>
      <md-select 
        v-model="product" 
        name="products" 
        id="products"
      >
        <md-option 
           v-for="(product, index) in products"
           :key="index"
           :value="product.sku"
         >
          {{product.name}}
        </md-option>
      </md-select>
    </md-field>

    <md-field>
      <label>Quantity</label>
      <md-input 
        v-model="quantity"
        type="number"
        :min="1"
      />
    </md-field>

    <div>
      <md-radio v-model="type" :value="1">Stocked In</md-radio>
      <md-radio v-model="type" :value="0">Stocked Out</md-radio>
    </div>

    <md-card-actions>
      <md-button class="md-primary">Submit</md-button>
    </md-card-actions>
  </form>
</template>

<script>
export default {
  name: "TransactionForm",
  props: ['products'],
  data: function() {
    return {
      product: "",
      type: 1,
      quantity: ""
    }
  }
}
</script>
