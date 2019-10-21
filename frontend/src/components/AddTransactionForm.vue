<template>
  <form class="md-card transaction-form" @submit="submitForm">
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
           :value="product.id"
         >
          {{product.name}}
        </md-option>
      </md-select>
    </md-field>

    <md-field :class="quantityErrorMessage">
      <label>Quantity</label>
      <md-input 
        v-model="quantity"
        type="number"
        @change="resetError"
        required
        :min="1"
      />
      <span class="md-error">{{quantityMessage}}</span>
    </md-field>

    <div>
      <md-radio v-model="type" :value="1">Stock In</md-radio>
      <md-radio v-model="type" :value="0">Stock Out</md-radio>
    </div>

    <md-card-actions>
      <md-button type="submit" class="md-primary">Submit</md-button>
    </md-card-actions>
  </form>
</template>

<script>
import Vue from 'vue';

export default {
  name: "TransactionForm",
  props: ['products'],
  data: function() {
    return {
      product: "",
      type: 1,
      quantity: "",
      quantityError: false,
      quantityMessage: ""
    }
  },
  methods: {
        submitForm: function(event) {
            event.preventDefault();
            const data = {
                "product"   : this.product,
                "quantity"  : this.quantity,
                "date"      : new Date(),
                "transactionType" : this.type
            }
            Vue.axios.post("http://localhost:8000/transaction/", data)
            .then(e => {
                if(e){
                    this.$emit("add-success", true);
                    this.quantity = "";
                }
            }).catch(event => {
                if(event.response) {
                    const { quantity } = event.response.data;

                    if(quantity) {
                        this.quantityError = true;
                        this.quantityMessage = quantity[0].charAt(0).toUpperCase() + quantity[0].slice(1);
                    }
                }
            })
        },
        resetError: function() {
            this.quantityError = false;
            this.quantityMessage = "";
        }
  },
  computed: {
        quantityErrorMessage: function() {
            return {
                'md-invalid': this.quantityMessage
            }
        }
    }
}
</script>
