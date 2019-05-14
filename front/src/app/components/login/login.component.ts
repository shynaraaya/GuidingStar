import { Component, OnInit } from '@angular/core';
<<<<<<< HEAD
import { Router } from '@angular/router'
import {ProviderService} from '../../shared/services/provider.service'
import {IAuthResponse} from  '../../shared/modules/models'
=======
import {Router} from '@angular/router';
import {ProviderService} from '../../shared/services/provider.service';
>>>>>>> 8e2fc6d35b92d0d72f425865667caba6c689858c

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
<<<<<<< HEAD
export class LoginComponent implements OnInit {
  public signupname: any = '';
  public signuppassword: any = '';
  public username = '';
  public password = '';
  public email = '';
  public logged = false;
  public isStaff = false;
  public loggedUsername = '';
  ngOnInit(){
  }

  constructor(private provider: ProviderService, private router: Router) { }


  hideModal = () => {
    this.router.navigateByUrl('').then();
  }

  auth() {
    if (this.username !== '' && this.password !== '') {
      this.provider.auth(this.username, this.password).then(res => {
        localStorage.setItem('token', res.token);
        this.isStaff = res.is_staff;
        this.logged = true;
        this.loggedUsername = res.username;
        this.username = '';
        this.password = '';
        // this.provider.getCategories().then(r => {
        //   this.categories = r;
        // });
=======
export class LoginComponent {
  provider:ProviderService;
  public authorized = false;
  
  public login:any = '';
  public password:any = ''; 

  constructor(private prov: ProviderService) {
  }
  

  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.authorized = true;
    }

    if (this.authorized) {
      console.log(token);
    }

  }
  auth() {
    if (this.login !== '' && this.password !== '') {
      console.log(this.login + this.password);
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);
        this.authorized = true;
>>>>>>> 8e2fc6d35b92d0d72f425865667caba6c689858c
      });
    }
  }

<<<<<<< HEAD
  isAdmin() {
    this.provider.getMe().then( res => {
      this.provider.isAdmin = res.is_superuser;
    });
  }
}

=======
  logout() {
    this.provider.logout().then(res => {
      this.authorized = false;
      localStorage.clear();
    });
  }
}
>>>>>>> 8e2fc6d35b92d0d72f425865667caba6c689858c
