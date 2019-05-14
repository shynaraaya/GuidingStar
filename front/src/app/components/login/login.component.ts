import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'
import {ProviderService} from '../../shared/services/provider.service'
import {IAuthResponse} from  '../../shared/modules/models'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
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
      });
    }
  }

  isAdmin() {
    this.provider.getMe().then( res => {
      this.provider.isAdmin = res.is_superuser;
    });
  }
}

