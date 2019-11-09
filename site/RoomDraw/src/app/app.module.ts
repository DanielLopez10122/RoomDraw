import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { GroupComponent } from './components/group/group.component';
import { NavBarComponent } from './components/nav-bar/nav-bar.component';
import { HousingComponent } from './components/housing/housing.component';

@NgModule({
	declarations: [
		AppComponent,
		HomeComponent,
		GroupComponent,
		NavBarComponent,
		HousingComponent
	],
	imports: [
		BrowserModule,
		AppRoutingModule,
		HttpClientModule
	],
	providers: [],
	bootstrap: [AppComponent]
})
export class AppModule { }
