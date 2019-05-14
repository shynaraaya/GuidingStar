import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import {ProviderService} from '../../shared/services/provider.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
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
      });
    }
  }

  logout() {
    this.provider.logout().then(res => {
      this.authorized = false;
      localStorage.clear();
    });
  }
}