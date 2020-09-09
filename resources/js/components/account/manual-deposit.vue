<template>
    <div>
        <article class="heading-component">
            <div class="heading-component-inner">
                <h5 class="heading-component-title">
                </h5>
                <div class="heading-component-aside">

                </div>
            </div>
        </article>
        <div class="alert alert-success" v-show="success_message">
                    <p>{{ success_message }}</p>
        </div>
         <div class="alert alert-warning" v-show="error_message">
                    {{ error_message }}
        </div>
        <form class="rd-form" @submit.prevent="manualPayment()">
        <div class="card-form card-form-login">
            <div class="alert alert-info">
                    <p class="text"><strong>Be informed</strong> that your wallet will be credited as soon as we receive your payment.</p>
                </div>
            
                <input class="form-control mt-2" type='text' placeholder='Amount to deposit' v-on:keyup="bankDetail" v-model="info.amount"><br>
                <input  class="form-control mt-6" type="text" placeholder="Account holder's name" v-on:keydown="bankDetail" v-model="info.fullName"><br>
                
            
        </div>
        <br>
        <div class="card-form card-form-login" v-show='check'>
            <h5>Make a Transfer or direct deposit into this account</h5><br>
            <div >
                <p><b>Account Name:</b> Charris Global Enterprise</p>
                <p><b>Account Number:</b> 5600577784</p>
                <p><b>Bank Name:</b> Fidelity Bank</P>
            </div>
        </div>
        <br>
        <div  class="card-form card-form-login" v-show='check'>
            <p style='color:#ff0000'>Ensure you have made payment before clicking this button!</p><br>
            <input :disabled='is_loading' type='submit' class="btn btn-success mt-6" value="Payment Complete">
            <p v-show="is_loading" style="color:#00ff00"><i>processing...</i></p>
        </div>
        </form>

    </div>
</template>
<script>
export default {
    data(){
        return{
            info:{
                amount:'',
                fullName:''
            },
            check: false,
            is_loading:false,
            success_message:'',
            error_message:''
            
        }
    },
    methods:{
        bankDetail(){
            if(this.info.amount!='' && this.info.fullName!=''){
                this.check = true
            }
            if(this.info.amount=='' || this.info.fullName==''){
                this.check = false
            }
        },
        manualPayment(){
            this.is_loading = true
            axios.post('/account/api/manualdepositapi',{
                sender:this.info.fullName,
                amount:this.info.amount,
            } )
            .then(data=>{
                this.is_loading = false
                this.success_message = data.data.response
            })
            .catch(err=>{
                console.log(err)
                this.error_message = 'Something went wrong, ensure you have good internet connection and try again'
                this.is_loading = false
            })
            
        }
    },
    
}
</script>
<style scoped>
p{
    font-size:14px;
}

</style>