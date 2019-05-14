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

export interface IAuthResponse{
  token: string;
}

