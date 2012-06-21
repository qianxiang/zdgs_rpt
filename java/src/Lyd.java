import java.util.List;


public class Lyd implements IReport  {
	public String lyd_no;
	public String lldw;
	public String lllb;
	public String lydbh;
	public String llck;
	public String llrq;
	
	private List <LydDetail> lydList;
	public List<LydDetail> getList() {
		return lydList;
	}
	public void setLydList(List<LydDetail> lydList) {
		this.lydList = lydList;
	}

	
}
