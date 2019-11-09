import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { GroupComponent } from './components/group/group.component';
import { HousingComponent } from './components/housing/housing.component';

const routes: Routes = [
	{ path: 'housing', component: HousingComponent },
	{ path: 'group', component: GroupComponent },
	{ path: 'home', component: HomeComponent },
	{ path: '', redirectTo: '/home', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
