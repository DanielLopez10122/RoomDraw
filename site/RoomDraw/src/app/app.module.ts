import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { GroupComponent } from './group/group.component';
import { NavBarComponent } from './nav-bar/nav-bar.component';
import { HousingComponent } from './housing/housing.component';
import { DocumentComponent } from './document/document.component';
import { FaqComponent } from './faq/faq.component';

@NgModule({
	declarations: [
		AppComponent,
		HomeComponent,
		GroupComponent,
		NavBarComponent,
		HousingComponent,
		DocumentComponent,
		FaqComponent
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
