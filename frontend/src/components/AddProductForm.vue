<template>
  <form class="md-card product-form" @submit="submitForm">
    <md-card-header>
        <h1 class="md-title">Add Product</h1>
    </md-card-header>
    <md-field :class="nameErrorMessage">
        <label>Name</label>
        <md-input 
            v-model="name" 
            @change="resetError"
            required
        />
      <span class="md-error">{{nameMessage}}</span>
    </md-field>
    <md-field :class="skuErrorMessage">
        <label>SKU</label>
        <md-input 
            v-model="sku" 
            @change="resetError"
            required
        />
      <span class="md-error">{{skuMessage}}</span>
    </md-field>
    <md-card-actions>
      <md-button type="submit" class="md-primary">Submit</md-button>
    </md-card-actions>
  </form>
</template>

<script>
import Vue from 'vue';

export default {
  name: "ProductForm",
  data: function() {
    return {
        name: "",
        sku: "",
        nameError: false,
        nameMessage: "",
        skuError: false,
        skuMessage: "",
    }
  },
  methods: {
    resetError: function () {
        this.nameError =  false;
        this.nameMessage =  "";
        this.skuError =  false;
        this.skuMessage = "";
    },
    submitForm: function(event) {
        event.preventDefault();
        const data = {
            "name": this.name,
            "sku" : this.sku
        }
        Vue.axios.post("http://localhost:8000/product/", data)
        .then(e => {
            if(e){
                this.$emit("add-success", true);
                this.name = "";
                this.sku  = "";
            }
        }).catch(event => {
            if(event.response) {
                const { sku, name } = event.response.data;

                if(name) {
                    this.nameError = true;
                    this.nameMessage = name[0].charAt(0).toUpperCase() + name[0].slice(1);
                }

                if(sku) {
                    this.skuError = true;
                    this.skuMessage = sku[0].charAt(0).toUpperCase() + sku[0].slice(1);
                }
            }
        })
    }
  },
  computed: {
        nameErrorMessage: function() {
            return {
                'md-invalid': this.nameMessage
            }
        },
        skuErrorMessage: function() {
            return {
                'md-invalid': this.skuMessage
            }
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
