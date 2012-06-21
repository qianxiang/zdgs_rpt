import java.util.List;


public class Sld implements IReport  {
	public String sld_no;
	public String hth;
	public String gldw;
	public String slgj;
	public String xmh;
	public String slbh;
	public String fph;
	public String zbrq;
	public String slrq;
	public String slck;
	private List <SldDetail> sldList;
	public List<SldDetail> getList() {
		return sldList;
	}
	public void setSldList(List<SldDetail> sldList) {
		this.sldList = sldList;
	}

	
}
