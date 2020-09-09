<template>
    <div class="row row-50 justify-content-center">
        <div class="col-md-10 col-lg-8 col-xl-5">
            <complete-profile-details :user_data="userData"></complete-profile-details>
        </div>
    </div>
</template>

<script>
    import otp from './otp-view';
    import CompleteProfileDetails from './complete-register';
    import newUserReg from './newUserReg'
    export default {//
        props: [],
        data() {
            return {
                // phone: '',
                // // calling_code: '234',
                // current_view: 2, // 1 for form view as it is needed before otp is requested, 2 for otp view
                // non_field_errors: '',
                // userData: [],
                // is_loading: false
            }
        },
        components: {
            otp,
            CompleteProfileDetails
        },
        methods: {
            // register: function () {
            //     this.is_loading = true
            //     let phone = this.phone
            //     let calling_code = this.calling_code

            //     axios.post('/users/request-otp', {phone: phone})
            //         .then((resp) => {
            //             this.userData = resp.data;
            //             this.enableOTPVIew()})
            //         .catch((err) => {
            //             this.is_loading = false;
            //             this.non_field_errors = err.response.data.non_field_errors instanceof Array ? err.response.data.non_field_errors[0] : err.response.data.non_field_errors
            //         })
            // },
            // enableOTPVIew: function () {
            //     this.is_loading = false;
            //     this.current_view = 2
            // }
        }
    }
</script>

<style scoped>
    .__sport_preloader {
        display: flex;
        justify-content: center;
        flex-direction: row;
        text-align: center;
    }

    .preloader-body.reduced {
        height: 25px;
        width: 25px;
    }
</style>