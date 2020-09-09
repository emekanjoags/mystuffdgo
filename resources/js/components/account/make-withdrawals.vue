<template>
    <div class="col-xl-8">
        <!-- Heading Component-->
        <article class="heading-component">
            <div class="heading-component-inner">
                <h5 class="heading-component-title">
                </h5>
                <div class="heading-component-aside">

                </div>
            </div>
        </article>
        <div class="card-top-panel">
            <div class="card-top-panel-left">
                <h5 class="card-title card-title-login" v-if="!allow_edit && !show_password_view">Request Withdrawal</h5>
                <h5 class="card-title card-title-login" v-else>Edit Bank Details</h5>
            </div>
        </div>
        <div class="card-form card-form-login">
            <form class="rd-form" @submit.prevent="submitRequest()" v-if="!show_password_view">
                <div class="alert alert-info">
                    <strong>Be informed</strong> that any withdrawal below NGN 1,000 will incur a charge of NGN 50.
                </div>


                <div class="alert alert-warning" v-show="error_survey">
                            {{ error_survey }}
                </div>
                <div class="alert alert-success" v-show="success_survey">
                                {{ success_survey }}
                </div>

                
                <div class="alert alert-warning" v-show="error_message">
                    {{ error_message }}
                </div>
                <div class="alert alert-success" v-show="success_message">
                    {{ success_message }}
                </div>
                <div class="form-wrap">
                    <input type="tel" class="form-input" placeholder="Enter Amount" v-model="amount" @input="amountMessage" maxlength="5">
                    <div class="form-output error" v-if="amount_error">
                        {{amount_error}}
                    </div>
                </div>
                <div class="d-flex justify-content-end" v-if="allow_edit === false">
                    <button type="button" class="btn btn-link" @click="enableEdit"><small>Edit Withdrawal details</small></button>
                </div>
                <div class="form-wrap">
                    <label>Bank Name</label>
                    <select class="form-input" v-model="wallet_details.bank_name" :required="true" @change="selectBank($event)">
                        <option v-for="(bank, index) in banks" :value="bank.name" :bank_code="bank.code" :disabled="!allow_edit" :selected="bank.name === wallet_details.bank_name">{{bank.name}}</option>
                    </select>
                </div>
                <div class="form-wrap">
                    <input class="form-input" placeholder="Account Holder Name" type="text" v-model="wallet_details.account_name"
                           name="form-input" :readonly="!allow_edit">
                </div>
                <div class="form-wrap">
                    <input class="form-input" placeholder="Account Number" type="tel" v-model="wallet_details.account_number"
                           name="form-input" :readonly="!allow_edit">
                </div>

                <button v-if="survey_btn" class="button button-primary button-block d-flex justify-content-between" :data-target="modal" 
                data-toggle="modal" type="button">
                    <span>Submit</span>
                </button>

                
                <button class="button button-primary button-block d-flex justify-content-between" type="submit"
                        :disabled="is_loading" v-else>
                    <div class="__sport_preloader" v-if="is_loading">
                        <div class="preloader-body reduced">
                            <div class="preloader-item"></div>
                        </div>
                    </div>
                    <span>Withdraw</span>
                </button>

            </form>
           

            <form @submit.prevent="checkPassword" v-else>
                <div class="alert alert-warning" v-show="password_error_message">
                    {{ password_error_message }}
                </div>
                <div class="form-wrap position-relative">
                    <input class="form-input" placeholder="Enter Login Password" type="password" v-model="password"
                           name="form-input" id="login-password">
                    <span @click="passwordVisibilityToggle" class="position-absolute password-eye">
                                <span class="fa fa-eye" v-if="password_stat"></span>
                                <span class="fa fa-eye-slash" v-else></span>
                            </span>
                </div>
                <button class="button button-primary button-block d-flex justify-content-between" type="submit"
                        :disabled="password_loading">
                    <div class="__sport_preloader" v-if="password_loading">
                        <div class="preloader-body reduced">
                            <div class="preloader-item"></div>
                        </div>
                    </div>
                    <span>Validate Password</span>
                </button>
            </form>

        </div>

        <!-- surveyform -->
            <div id="bio-data" class="modal fade" role="dialog">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h6 class="modal-title">This is a short survey to help us serve you better</h6>
                            
                        </div>
                        
                         
                        <div class="modal-body">
                            <form class="rd-form" @submit.prevent="submitSurvey()">
                                <div class="form-wrap">
                                    <label>Select Your gender</label>
                                    <select v-model="survey.gender" class="form-input" :required="true" @change="finish">
                                        <option value="male">Male</option>
                                        <option value='female'>Female</option>
                                        <option value='other'>other</option>
                                    </select>
                                </div>

                                <div class='form-wrap'>
                                    <label>May we know your age bracket?</label>
                                    <select v-model="survey.age" class="form-input" :required="true" @change="finish">
                                        <option value="18-25">18-25</option>
                                        <option value="26-40">26-40</option>
                                        <option value="41 and above">41 and above</option>
                                    </select>
                                </div>

                                <div class='form-wrap'>
                                    <label>Select your country of residence</label>
                                    <select v-model="survey.country" class="form-input"  :required="true" @change="finish">
                                        <option value="nigeria" selected>Nigeria</option>
                                    </select>
                                </div>
                                <div class='form-wrap'>
                                    <label>Select your state of residence</label>
                                    <select v-model="survey.state" class="form-input" :required="true" @change="finish">
                                        <option v-for="state in states" :value="state">{{state}}</option>

                                    </select>
                                </div>
                                <div class='form-wrap'>
                                    <label>How did you hear about us?</label>
                                    <select v-model="survey.discovery" class="form-input" :required="true" @change="finish">
                                        <option value="telegram">Telegram</option>
                                        <option value="facebook">Facebook</option>
                                        <option value="twitter">Twitter</option>
                                        <option value="friend">From a friend</option>
                                        <option value="other">other</option>

                                    </select>
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-danger" data-dismiss="modal" :disabled="is_loading">Close
                                    </button>
                                    <button id="finish_btn" type="button" class="btn btn-success" data-dismiss='modal' :disabled="incomplete" @click="submitSurvey()">Finish
                                    </button>
                                    <p v-show="is_loading" style="color:#00ff00"><i>processing...</i></p>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
                
                
            </div>

            
        <!-- questionform -->
            <div id="question" class="modal fade" role="dialog">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h6 class="modal-title">This is a short survey to help us serve you better</h6>
                            
                        </div>
                        
                         
                        <div class="modal-body">
                            <form class="rd-form" @submit.prevent="submitAnswer()">
                                <div class="form-wrap">
                                    <label>{{question}}</label>
                                    <input class="form-input" type="text" v-model="answer" v-on:keyup="question_finish()">
                                </div>

                                <div class="modal-footer">
                                    <button type="button" class="btn btn-danger" data-dismiss="modal" :disabled="is_loading">Close
                                    </button>
                                    <button  id="second_finish_btn" type="button" class="btn btn-success" data-dismiss='modal' :disabled="incomplete" @click="submitAnswer()">Finish
                                    </button>
                                    <p v-show="is_loading" style="color:#00ff00"><i>processing...</i></p>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
                
                
            </div>
            <!--end of question form-->
    </div>
</template>

<script>
    import {Money} from 'v-money'

    export default {
        name: "make-withdrawals",
        props: ['balance'],
        data() {
            return {
                states:[
  "Abia",
  "Adamawa",
  "Akwa Ibom",
  "Anambra",
  "Bauchi",
  "Bayelsa",
  "Benue",
  "Borno",
  "Cross River",
  "Delta",
  "Ebonyi",
  "Edo",
  "Ekiti",
  "Enugu",
  "FCT - Abuja",
  "Gombe",
  "Imo",
  "Jigawa",
  "Kaduna",
  "Kano",
  "Katsina",
  "Kebbi",
  "Kogi",
  "Kwara",
  "Lagos",
  "Nasarawa",
  "Niger",
  "Ogun",
  "Ondo",
  "Osun",
  "Oyo",
  "Plateau",
  "Rivers",
  "Sokoto",
  "Taraba",
  "Yobe",
  "Zamfara"
],
                survey:{
                    gender:'',
                    age:'',
                    country:'',
                    state:'',
                    discovery:''
                },
                survey_btn:true,
                success_survey:null,
                error_survey:null,
                incomplete:true,
                answer:'',
                modal: '#bio-data',
                question:'',
                password_loading: false,
                show_password_view: false,
                password: '',
                error_message: null,
                password_error_message: null,
                password_success_message: null,
                success_message: null,
                allow_edit: false,
                money: {
                    decimal: '.',
                    thousands: ',',
                    prefix: '₦ ',
                    suffix: '',
                    precision: 2,
                    masked: false
                },
                wallet_details: {
                    bank_name: null,
                    account_name: null,
                    account_number: null,
                    bank_code: null
                },
                amount: 0,
                is_loading: false,
                banks: [],
                amount_error: '',
                password_stat: true,
                page_title: 'Request Withdrawal'
            }
        },
        methods: {
            finish(){
                if(this.survey.gender!='' && this.survey.country!='' && this.survey.state1!='' && this.survey.age!='' && this.survey.discovery!=''){
                    document.getElementById('finish_btn').style.opacity = '1'
                    this.incomplete = false
                }
            },

            question_finish(){
                if (this.answer!=''){
                    document.getElementById('second_finish_btn').style.opacity = '1'
                    this.incomplete = false
                }
            },

            submitAnswer(){
                this.success_survey = ''
                this.error_survey = ''
                this.loading = true
                axios.post('/account/api/question', {
                    answer:this.answer,
                    question:this.question
                })
                .then(resp=>{
                    this.loading = false
                    this.survey_btn = false
                    this.success_survey = resp.data.response
                    this.error.survey = ''
                })
                .catch(err=>{
                    if(err.response){
                        this.is_loading = false
                        this.error_survey ='Something went wrong, check your internet connection and try again.'
                    }
                    
                })
            },

            submitSurvey(){
                this.success_survey = ''
                this.error_survey = ''
                this.loading = true
                axios.post('/account/api/survey', {
                    gender:this.survey.gender,
                    age:this.survey.age,
                    country:this.survey.country,
                    state:this.survey.state,
                    discovery:this.survey.discovery
                })
                .then(resp=>{
                    this.loading = false
                    this.survey_btn = false
                    this.success_survey = resp.data.response
                    this.error.survey = ''
                    
                })
                .catch(err=>{
                    if(err.response){
                        this.loading = false
                        this.error_survey ='Something went wrong, check your internet connection and try again.'
                        this.success.survey = ''
                    }
                })
            },
            passwordVisibilityToggle(){
                this.password_stat = !this.password_stat;
                showPassword('login-password')
            },
            selectBank(event){
                this.wallet_details.bank_code = event.target.options[event.target.selectedIndex].attributes['bank_code'].value
            },
            getWalletDetails() {
                axios.get('/account/wallet').then((resp) => {
                    this.wallet_details.bank_name = resp.data.bank_name
                    this.wallet_details.account_name = resp.data.bank_account_name
                    this.wallet_details.account_number = resp.data.bank_account_number
                    this.wallet_details.bank_code = resp.data.bank_code

                    if((!this.wallet_details.bank_name || this.wallet_details.bank_name == '') && (!this.wallet_details.account_name || this.wallet_details.account_name == '') && (!this.wallet_details.account_number || this.wallet_details.account_number == '') && (!this.wallet_details.bank_code || this.wallet_details.bank_code == '')){
                        this.allow_edit = true
                    }
                    console.log(this.allow_edit)
                }).catch((err) => console.log(err))
            },
            submitRequest() {
                this.is_loading = true
                this.success_message = ''
                this.error_message = ''
                let formData = {
                    bank_code: this.wallet_details.bank_code,
                    amount: this.amount,
                    bank_name: this.wallet_details.bank_name,
                    account_name: this.wallet_details.account_name,
                    account_number: this.wallet_details.account_number
                };

                axios.post('/account/api/withdraw', formData).then((rep) => {
                    this.success_message = 'Withdrawal request sent!';
                    setTimeout(() => window.location = '/account', 2000)
                }).catch((err) => {
                    if(err.response){
                        this.is_loading = false
                        console.log(err.response.data.response)
                        this.error_message = err.response.data.response
                    }
                })
            },
            getBanks() {
                axios.get('/account/api/banks').then((resp) => {
                    this.banks = resp.data
                }).catch((err) => console.log(err))
            },
            enableEdit(){
                this.show_password_view = true
                // this.allow_edit = true
            },
            checkPassword(){
                this.password_loading = true
                axios.post('/account/api/password-check', {password: this.password}).then((resp) => {
                    this.allow_edit = true
                    this.password_loading = false
                    this.show_password_view = false
                }).catch((err) => {
                    if(err.response){
                        this.password_loading = false
                        this.password_error_message = err.response.data.response
                    }
                })
            },
            amountMessage(){
                this.amount_error = ''
                let amount = this.amount;
                if(amount < 1000){
                    amount = amount + 50
                }

                if(Number(this.amount) <= 999.99){
                    this.amount_error = `An additional carrier fee of NGN 50 will be applied when you withdraw less than NGN 1,000, your current available balance is: NGN ${this.balance}`
                }else if(amount > this.balance){
                    this.amount_error = `This amount has exceeded your available balance of NGN ${this.balance}, please try a lesser amount.`
                }

            },
            getSurvey(){
                axios.get('/account/api/survey')
                .then(resp=>{
                    if(resp.data.response=='true'){
                        this.modal = "#question"
                    }
                })
                .catch(err=>{
                    console.log('error')
                    console.log('error: ' + err)
                })
            },
            getQuestion(){
                axios.get('/account/api/question')
                .then(resp=>{
                    if(resp.data.response=='true' && this.modal=='#question'){
                        this.survey_btn = false
                    }
                    this.question = resp.data.question
                })
            }
        },
        created() {
            this.getSurvey()
            this.getQuestion()
            this.getBanks()
            this.getWalletDetails()
            
        },
        computed: {
            amountInKobo() {
                return this.amount * 100
            }
        },
        components: {
            Money
        },
    }
</script>

<style scoped>
#finish_btn{
    opacity:0.5
}
#second_finish_btn{
    opacity:0.5
}

</style>