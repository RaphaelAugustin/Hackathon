import { GUIPage } from './app.po';

describe('gui App', function() {
  let page: GUIPage;

  beforeEach(() => {
    page = new GUIPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
