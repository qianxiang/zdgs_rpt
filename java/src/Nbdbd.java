import java.util.List;


public class Nbdbd implements IReport  {
	public String nbdbd_no;
	public String yjbh;
	public String tbrq;
	public String brkf;
	public String bcck;
	public String shlxr;
	public String lxrdh;
	public String shdz;
	public String shrq;
	private List <NbdbdDetail> nbdbdList;
	public List<NbdbdDetail> getList() {
		return nbdbdList;
	}
	public void setNbdbdList(List<NbdbdDetail> nbdbdList) {
		this.nbdbdList = nbdbdList;
	}

	
}
