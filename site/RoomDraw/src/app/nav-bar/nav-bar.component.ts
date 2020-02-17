import { GroupService } from '../group.service';
import { Component, OnInit } from '@angular/core';
import { Invitations } from '../Invitations';

@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.css']
})
export class NavBarComponent implements OnInit {

  invitations: Invitations[];

  constructor(
    private groupService: GroupService
  ) { }

  ngOnInit() {
    this.groupService.getInvites()
      .subscribe(invitations => this.invitations = invitations);
  }

}
