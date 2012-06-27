import javax.servlet.*;
import javax.servlet.http.*;

public class ReportServlet extends HttpServlet {

	private static final long serialVersionUID = -6575580649791881116L;

	private String webPath = "";
	private DateReader dateReader = new DateReader();

	public void service(HttpServletRequest req, HttpServletResponse res)
			throws ServletException {
		String reportid = req.getParameter("id");
		String reportType = req.getParameter("type");
		REPORTTYPE repType = REPORTTYPE.valueOf(reportType);
		String pdffile;
		webPath = getServletContext().getRealPath(".");
		try {
			pdffile = pdfBuilder(reportid, repType);
			res.sendRedirect(pdffile);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public enum REPORTTYPE {
		fld, sld, jld, lyd, nbdbd, rkd
	};

	private String pdfBuilder(String reportid, REPORTTYPE reportType)
			throws Exception {
		String templateName = "balnk.pdf";
		IReport report = null;
		switch (reportType) {
		case fld:
			report = dateReader.readerFld(reportid);
			templateName = "fld.pdf";
			break;
		case sld:
			report = dateReader.readerSld(reportid);
			templateName = "sld.pdf";
			break;
		case jld:
			report = dateReader.readerJld(reportid);
			templateName = "jld.pdf";
			break;
		case lyd:
			report = dateReader.readerLyd(reportid);
			templateName = "lyd.pdf";
			break;
		case nbdbd:
			report = dateReader.readerNbdbd(reportid);
			templateName = "nbdbd.pdf";
			break;
		case rkd:
			report = dateReader.readerRkd(reportid);
			templateName = "rkd.pdf";
			break;
		}

		String templatePath = webPath + "/template/" + templateName;
		String dest = "";
		synchronized (dest) {
			// dest = "dest/"+System.currentTimeMillis() + ".pdf";
			dest = "dest/" + reportid + ".pdf";
		}
		PdfFiels.manipulatePdf(templatePath, webPath + "/" + dest, report);
		return dest;
	}
}
