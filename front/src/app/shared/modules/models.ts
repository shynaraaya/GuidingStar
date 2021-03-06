import {Time} from '@angular/common';

export interface Review {
  id: number;
  review: string;
  rating: number;
  author: string;
  submissionDate: Date;
}

export interface Flight {
  id: number;
  companyName: string;
  sourceLocation: string;
  destinationLocation: string;
  departureDate: Date;
  departureTime: Time;
  fareEconomy: any;
  fareBusiness: any;
  fareFirst: any;
  numSeatsRemainingEconomy: number;
  numSeatsRemainingBusiness: number;
  numSeatsRemainingFirst: number;
}

export interface Hotel {
  id: number;
  poster: string;
  dailyCost: any;
  address: string;
  city: string;
  companyName: string;
  rating: number;
}

export interface HotelList {
  id: number;
  name: string;
}

export interface FlightList {
  id: number;
  name: string;
}

<<<<<<< HEAD
export interface User{
  username: string; 
  password: string;
}

export interface IAuthResponse{
  token: string;
  is_staff: boolean;
  username: string;
}
=======
export interface IAuthResponse{
  token: string;
}

>>>>>>> 8e2fc6d35b92d0d72f425865667caba6c689858c
