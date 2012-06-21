import java.util.List;

public class Rkd implements IReport {
	public String rkd_no;
	public String hth;
	public String ghdw;
	public String slck;
	public String slrq;
	public String rkdh;
	
	private List<RkdDetail> rkdList;

	public String getRkd_no() {
		return rkd_no;
	}

	public void setRkd_no(String rkd_no) {
		this.rkd_no = rkd_no;
	}

	public String getHth() {
		return hth;
	}

	public void setHth(String hth) {
		this.hth = hth;
	}

	public String getGhdw() {
		return ghdw;
	}

	public void setGhdw(String ghdw) {
		this.ghdw = ghdw;
	}

	public String getRkdh() {
		return rkdh;
	}

	public void setRkdh(String rkdh) {
		this.rkdh = rkdh;
	}

	public String getSlck() {
		return slck;
	}

	public void setSlck(String slck) {
		this.slck = slck;
	}

	public String getSlrq() {
		return slrq;
	}

	public void setSlrq(String slrq) {
		this.slrq = slrq;
	}

	public List<RkdDetail> getRkdList() {
		return rkdList;
	}

	public List<RkdDetail> getList() {
		return rkdList;
	}

	public void setRkdList(List<RkdDetail> rkdList) {
		this.rkdList = rkdList;
	}

	

}
